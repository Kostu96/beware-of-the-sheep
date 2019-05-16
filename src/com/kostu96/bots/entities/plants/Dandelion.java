package com.kostu96.bots.entities.plants;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.utils.ImageManager.ImageID;
import com.kostu96.bots.utils.Point;

public class Dandelion extends Plant {
	private static final int STRENGTH = 0;
	
	public Dandelion(World world, Point position) {
		super(world, position, STRENGTH);
	}

	@Override
	public void collision(Entity other) {

	}

	@Override
	public ImageID getImageID() {
		return ImageID.DANDELION;
	}

}
