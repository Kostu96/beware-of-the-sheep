package com.kostu96.bots.entities.animals;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.utils.Point;

public class Wolf extends Animal {

	public Wolf(World world, Point position) {
		super(world, position, 9, 5);
	}

	@Override
	public void collision(Entity other) {

	}

}
