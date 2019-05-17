package com.kostu96.bots.entities.animals;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.utils.ImageManager.ImageID;
import com.kostu96.bots.utils.Point;

public class Wolf extends Animal {
	private static final int STRENGTH = 9;
	private static final int INITIATIVE = 5;

	public Wolf(World world, Point position) {
		super(world, position, STRENGTH, INITIATIVE);
	}

	@Override
	public void collision(Entity other) {

	}

	@Override
	public ImageID getImageID() {
		return ImageID.WOLF;
	}

}
