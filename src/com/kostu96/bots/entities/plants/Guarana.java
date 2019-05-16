package com.kostu96.bots.entities.plants;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.entities.animals.Animal;
import com.kostu96.bots.utils.ImageManager.ImageID;
import com.kostu96.bots.utils.Point;

public class Guarana extends Plant {
	private static final int STRENGTH = 0;

	public Guarana(World world, Point position) {
		super(world, position, STRENGTH);
	}

	@Override
	public void collision(Entity other) {
		if (other instanceof Animal) {
			other.addStrength(3);
			//std::string message = other.getClassName() + " has now " + std::to_string(other.getStrength()) + " Strength";
			//m_world.addMessage(std::move(message));
		}
	}

	@Override
	public ImageID getImageID() {
		return ImageID.GUARANA;
	}

}
