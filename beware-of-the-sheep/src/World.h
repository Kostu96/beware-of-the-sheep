#pragma once

namespace bots {

	/*!
		\brief	Class representing game world
		\author	Konstanty Misiak
	*/
	class World
	{
	public:
		World(unsigned int sizeX, unsigned int sizeY);

		inline unsigned int getSizeX() const { return m_sizeX; }
		inline unsigned int getSizeY() const { return m_sizeY; }
	private:
		unsigned int m_sizeX, m_sizeY;
	};

} // namespace bots
