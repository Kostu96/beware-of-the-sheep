package com.kostu96.bots.entities.plants;

import com.kostu96.bots.World;
import com.kostu96.bots.utils.ImageManager.ImageID;
import com.kostu96.bots.utils.Point;

public class Grass extends Plant {
	private static final int STRENGTH = 0;

	public Grass(World world, Point position) {
		super(world, position, STRENGTH);
	}

	@Override
	public ImageID getImageID() {
		return ImageID.GRASS;
	}

}
