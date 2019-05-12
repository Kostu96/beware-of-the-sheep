package com.kostu96.bots.entities.animals;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.utils.Point;

public class Antelope extends Animal {

	public Antelope(World world, Point position) {
		super(world, position, 4, 4);
	}

	@Override
	public void collision(Entity other) {

	}

}
