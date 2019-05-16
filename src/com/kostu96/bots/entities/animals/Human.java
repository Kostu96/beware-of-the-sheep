package com.kostu96.bots.entities.animals;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.utils.Point;

public class Human extends Animal {
	private static final int STRENGTH = 5;
	private static final int INITIATIVE = 4;

	public Human(World world, Point position) {
		super(world, position, STRENGTH, INITIATIVE);
	}

	@Override
	public void collision(Entity other) {

	}

}