#pragma once
#include "pch.h"
#include "Point.h"

namespace bots {

	class Area
	{
	public:
		using NeighboursArray = std::array<Point, 4>;

		Area(unsigned int width, unsigned int height);
		Area(const Area &) = delete;
		~Area();

		void put(unsigned int x, unsigned int y, const std::string & str);
		void put(const Point & position, const std::string & str);

		void clear();
		void print() const;

		unsigned int getFreeSpaceAround(Point position, NeighboursArray & arr) const;
	private:
		unsigned int getInnerIndex(Point position) const;

		unsigned int m_width, m_height;
		char * m_arr;
	};

} // namespace bots
