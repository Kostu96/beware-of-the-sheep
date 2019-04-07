#include "Area.h"
#include <exception>
#include <cstring>
#include <iostream>

namespace bots {

	Area::Area(unsigned int width, unsigned int height) :
		m_width(width), m_height(height),
		m_arr(new char[2 * width * height + height])
	{
	}

	Area::~Area()
	{
		delete[] m_arr;
	}

	void Area::put(unsigned int x, unsigned int y, const char * str)
	{
		if (strlen(str) != 2)
			throw std::exception("Entity symbol must have 2 characters!");

		if (x >= 0 && x < m_width && y >= 0 && y < m_height)
		{
			m_arr[(2 * m_width + 1) * y + 2 * x] = str[0];
			m_arr[(2 * m_width + 1) * y + 2 * x + 1] = str[1];
		}
		else
			throw std::exception("Wrong position!");
	}

	void Area::put(const Point & position, const char * str)
	{
		if (strlen(str) != 2)
			throw std::exception("Entity symbol must have 2 characters!");

		unsigned int x = position.x;
		unsigned int y = position.y;
		if (x >= 0 && x < m_width && y >= 0 && y < m_height)
		{
			m_arr[(2 * m_width + 1) * y + 2 * x] = str[0];
			m_arr[(2 * m_width + 1) * y + 2 * x + 1] = str[1];
		}
		else
			throw std::exception("Wrong position!");
	}

	void Area::clear()
	{
		for (unsigned int i = 0; i < 2 * m_width + 1; ++i)
			for (unsigned int j = 0; j < m_height; ++j)
				if (i == 2 * m_width)
					m_arr[(2 * m_width + 1) * j + i] = ((j == m_height - 1) ? '\0' : '\n');
				else
					m_arr[(2 * m_width + 1) * j + i] = ' ';
	}

	void Area::print() const
	{
		std::cout << m_arr;
	}

	bool Area::isFreeSpaceAround() const
	{
		return false;
	}

} // namespace bots
