#pragma once
#include "Point.h"

namespace bots {

	class Area
	{
	public:
		Area(unsigned int width, unsigned int height);
		Area(const Area &) = delete;
		~Area();

		void put(unsigned int x, unsigned int y, const char * str);
		void put(const Point & position, const char * str);

		void clear();
		void print() const;
	private:
		unsigned int m_width, m_height;
		char * m_arr;
	};

} // namespace bots
