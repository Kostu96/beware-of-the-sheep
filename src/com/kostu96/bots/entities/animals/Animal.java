package com.kostu96.bots.entities.animals;

import java.util.Random;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.utils.Point;

public abstract class Animal extends Entity {
	
	public Animal(World world, Point position, int strength, int initiative) {
		super(world, position, strength, initiative);
	}

	@Override
	public void action() {
		Random rand = new Random();
		int vorh = rand.nextInt(1), norp = rand.nextInt(1);
		
		if (vorh == 1)
			move(0, norp == 1 ? -1 : 1);
		else
			move(norp == 1 ? -1 : 1, 0);
	}
}
