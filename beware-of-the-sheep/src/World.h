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

		void requestSpawn(Entity::Kind kind, Point position);
		inline void requestClose() { m_isRunning = false; }
	private:
		struct PendingSpawn
		{
			Entity::Kind kind;
			Point position;
		};

		void tick();

		void printLegend() const;
		void printSpacer() const;
		void print();

		void spawnPending();
		void spawnEntity(Entity::Kind kind, Point position);

		bool m_isRunning = true;
		unsigned int m_width, m_height;
		Area m_area;
		std::vector<Entity *> m_entities;
		std::vector<PendingSpawn> m_pendingSpawns;
	};

} // namespace bots
