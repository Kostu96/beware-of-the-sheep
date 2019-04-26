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
		Entity::Ptr getEntityAt(unsigned int x, unsigned int y);
		void spawnEntity(Entity::Kind kind, Point position);
		void addMessage(std::string && message) { m_messages.emplace_back(std::move(message)); }
	private:
		void removeKilledEntites();
		void sortEntities();

		void printLegend() const;
		void printSpacer() const;
		void printMessages();

		unsigned int m_width, m_height;
		Area m_area;
		std::vector<Entity::Ptr> m_entities;
		std::list<std::string> m_messages;
		bool m_isHumanTurn = false;
	};

} // namespace bots
