#pragma once
#include "Point.h"

namespace bots {
	
	/*!
		\brief	Class representing entities in the world.
		\author	Konstanty Misiak
	*/
	class Entity
	{
	public:
		virtual void action() = 0;
		virtual void collision(const Entity & other) = 0;
		virtual void draw() const = 0;

		const Point & getPosition() const { return m_position; }
		unsigned int getStrength() const { return m_strength; }
		unsigned int getInitiative() const { return m_initiative; }
	protected:
		void move(unsigned int x, unsigned int y) { m_position.x += x; m_position.y += y; }
	private:
		Point m_position;
		unsigned int m_strength;
		unsigned int m_initiative;
	};

} // namespace bots
