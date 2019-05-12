package com.kostu96.bots.entities.animals;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.utils.Point;

public class Fox extends Animal {

	public Fox(World world, Point position) {
		super(world, position, 3, 7);
	}

	@Override
	public void collision(Entity other) {

	}

}
