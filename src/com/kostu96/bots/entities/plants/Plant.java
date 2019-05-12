package com.kostu96.bots.entities.plants;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.utils.Point;

public abstract class Plant extends Entity {

	public Plant(World world, Point position, int strength) {
		super(world, position, strength, 0);
	}

}
