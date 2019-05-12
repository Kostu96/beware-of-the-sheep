package com.kostu96.bots.entities.animals;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.utils.Point;

public class Turtle extends Animal {

	public Turtle(World world, Point position) {
		super(world, position, 2, 1);
	}

	@Override
	public void collision(Entity other) {
		
	}

}
