package com.kostu96.bots.entities.animals;

import com.kostu96.bots.World;
import com.kostu96.bots.utils.ImageManager.ImageID;
import com.kostu96.bots.utils.Point;
import com.kostu96.bots.utils.Randmizer;

public class Turtle extends Animal {
	private static final int STRENGTH = 2;
	private static final int INITIATIVE = 1;

	public Turtle(World world, Point position) {
		super(world, position, STRENGTH, INITIATIVE);
	}

	@Override
	public void action() {
		int x = Randmizer.getInt(0, 4);
		if (x == 0)
			super.action();
	}
	
	@Override
	public boolean dodgedAttack(int strength) {
		return strength < 5;
	}
	
	@Override
	public ImageID getImageID() {
		return ImageID.TURTLE;
	}

}
