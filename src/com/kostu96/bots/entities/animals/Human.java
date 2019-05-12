package com.kostu96.bots.entities.animals;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.utils.Point;

public class Human extends Animal {

	public Human(World world, Point position) {
		super(world, position, 5, 4); // TODO add constants for strength and initiative in classes
	}

	@Override
	public void collision(Entity other) {

	}

}
