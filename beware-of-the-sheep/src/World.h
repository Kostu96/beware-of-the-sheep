#pragma once
#include "pch.h"
#include "Entities/Entity.h"
#include "Area.h"

namespace bots {

	/*!
		\brief	Class representing game world
		\author	Konstanty Misiak
	*/
	class World
	{
	public:
		World(unsigned int width, unsigned int height);

		void tick();
		void print();

		inline unsigned int getWidth() const { return m_height; }
		inline unsigned int getHeight() const { return m_width; }
		inline unsigned int getFreeSpaceAround(Point position, Area::NeighboursArray & arr) const { return m_area.getFreeSpaceAround(position, arr); }
		void spawnEntity(Entity::Kind kind, Point position);
	private:
		Entity::Ptr getEntityAt(unsigned int x, unsigned int y);
		void removeKilledEntites();
		void sortEntities();

		void printLegend() const;
		void printSpacer() const;

		unsigned int m_width, m_height;
		Area m_area;
		std::vector<Entity::Ptr> m_entities;
	};

} // namespace bots
