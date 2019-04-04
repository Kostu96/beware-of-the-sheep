#pragma once
#include "../Point.h"

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
		Entity(World & world, const Point & position, unsigned int strength = 0, unsigned int initiative = 0);
		virtual ~Entity() = default;

		virtual void action() = 0;
		virtual void collision(const Entity & other) = 0;
		void draw(Area & area) const;

		inline const Point & getPosition() const { return m_position; }
		inline unsigned int getStrength() const { return m_strength; }
		inline unsigned int getInitiative() const { return m_initiative; }
	protected:
		void move(unsigned int x, unsigned int y);
		
		virtual inline const char * getSymbol() const = 0;
	private:
		World & m_world;
		Point m_position;
		unsigned int m_strength;
		unsigned int m_initiative;
	};

} // namespace bots
