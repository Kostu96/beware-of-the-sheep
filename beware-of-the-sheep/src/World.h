#pragma once
#include "Entities/Entity.h"
#include "Area.h"
#include <vector>

namespace bots {

	/*!
		\brief	Class representing game world
		\author	Konstanty Misiak
	*/
	class World
	{
	public:
		World(unsigned int width, unsigned int height);
		~World();

		void simulate();

		inline unsigned int getWidth() const { return m_height; }
		inline unsigned int getHeight() const { return m_width; }
	private:
		void print();

		unsigned int m_width, m_height;
		Area m_area;
		std::vector<Entity *> m_entities;
	};

} // namespace bots
