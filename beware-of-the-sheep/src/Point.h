#pragma once

namespace bots
{
	/*!
		\brief	Point in worldspace
		\author	Konstanty Misiak
	*/
	struct Point
	{
		unsigned int x, y;

		std::string to_string() const
		{
			return "(" + std::to_string(x) + ", " + std::to_string(y) + ")";
		}
	};

} // namespace bots
