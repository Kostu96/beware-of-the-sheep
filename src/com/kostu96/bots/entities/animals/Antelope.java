package com.kostu96.bots.entities.animals;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.utils.ImageManager.ImageID;
import com.kostu96.bots.utils.Point;

public class Antelope extends Animal {
	private static final int STRENGTH = 4;
	private static final int INITIATIVE = 4;
	
	public Antelope(World world, Point position) {
		super(world, position, STRENGTH, INITIATIVE);
	}

	@Override
	public void collision(Entity other) {

	}

	@Override
	public ImageID getImageID() {
		return ImageID.ANTELOPE;
	}

}
