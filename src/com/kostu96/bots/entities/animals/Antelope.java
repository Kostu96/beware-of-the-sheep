package com.kostu96.bots.entities.animals;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.utils.Point;

public class Antelope extends Animal {

	public Antelope(World world, Point position, int strength, int initiative) {
		super(world, position, strength, initiative);
	}

	@Override
	public void collision(Entity other) {
		// TODO Auto-generated method stub

	}

}
