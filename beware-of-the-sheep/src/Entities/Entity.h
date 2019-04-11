#pragma once
#include "Point.h"

namespace bots {
	
	class World;
	class Area;

	/*!
		\brief	Class representing entities in the world.
		\author	Konstanty Misiak
	*/
	class Entity
	{
	public:
		enum class Kind {
			Antelope,
			CyberSheep,
			Fox,
			Human,
			Sheep,
			Turtle,
			Wolf,
			Bellandona,
			Dandelion,
			Grass,
			Guarana,
			Hogweed
		};

		Entity(World & world, const Point & position, unsigned int strength = 0, unsigned int initiative = 0);
		virtual ~Entity() = default;

		virtual void action() = 0;
		virtual void collision(Entity & other) = 0;
		void draw(Area & area) const;

		inline const Point & getPosition() const { return m_position; }
		inline unsigned int getStrength() const { return m_strength; }
		inline unsigned int getInitiative() const { return m_initiative; }
		inline unsigned int getLifeTime() const { return m_lifeTime; }
		inline bool isAlive() const { return m_isAlive; }

		inline void addStrength(unsigned int x) { m_strength += x; }
		inline void incrementLifeTime() { ++m_lifeTime; }
		inline void kill() { m_isAlive = false; }
	protected:
		void move(int x, int y);
		
		virtual inline const char * getSymbol() const = 0;
		virtual inline Kind getKind() const = 0;
		virtual inline const char * getClassName() const = 0;

		World & m_world;
	private:
		Point m_position;
		unsigned int m_strength;
		unsigned int m_initiative;
		unsigned int m_lifeTime = 0;
		bool m_isAlive = true;
	};

} // namespace bots
