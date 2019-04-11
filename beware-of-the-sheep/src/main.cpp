#include "pch.h"
#include "World.h"

int main()
{
	unsigned int width, height;
	std::cout << "Enter world size (X Y): ";
	std::cin >> width >> height;

	bots::World world(width, height);
	
	while (true)
	{
		world.print();
		world.tick();
	}

	return 0;
}

// TODO: move main loop into main
