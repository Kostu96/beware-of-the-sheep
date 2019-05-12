package com.kostu96.bots.entities.plants;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.utils.Point;

public class Dandelion extends Plant {

	public Dandelion(World world, Point position) {
		super(world, position, 0);
	}

	@Override
	public void collision(Entity other) {

	}

}
