package com.kostu96.bots.entities.plants;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.utils.Point;

public class Hogweed extends Plant {

	public Hogweed(World world, Point position, int strength) {
		super(world, position, strength);
	}

	@Override
	public void collision(Entity other) {

	}

}
