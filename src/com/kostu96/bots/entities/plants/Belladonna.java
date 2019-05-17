package com.kostu96.bots.entities.plants;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.entities.animals.Animal;
import com.kostu96.bots.utils.ImageManager.ImageID;
import com.kostu96.bots.utils.Point;

public class Belladonna extends Plant {
	private static final int STRENGTH = 99;

	public Belladonna(World world, Point position) {
		super(world, position, STRENGTH);
	}

	@Override
	public void collision(Entity other) {
		if (other instanceof Animal && other.getStrength() < getStrength()) {
			other.kill();
			
			// TODO: messages
			System.out.println(other.getClassName() + " was slain by " + getClassName());
		}
	}

	@Override
	public ImageID getImageID() {
		return ImageID.BELLADONA;
	}

}
