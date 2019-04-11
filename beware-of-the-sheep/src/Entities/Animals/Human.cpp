#include "pch.h"
#include "Human.h"


namespace bots {

	Human::Human(World & world, const Point & position) :
		Animal(world, position, 5, 4)
	{}

	void Human::action()
	{
		int x = _getch();
		if (x == 224) {
			int d = _getch();
			if (d == 72)
				move(0, -1);
			else if (d == 80)
				move(0, 1);
			else if (d == 75)
				move(-1, 0);
			else if (d == 77)
				move(1, 0);
		}
	}

} // namespace bots
