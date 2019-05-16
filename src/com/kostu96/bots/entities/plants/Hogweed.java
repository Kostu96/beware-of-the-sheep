package com.kostu96.bots.entities.plants;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.entities.animals.Animal;
import com.kostu96.bots.entities.animals.CyberSheep;
import com.kostu96.bots.utils.ImageManager.ImageID;
import com.kostu96.bots.utils.Point;

public class Hogweed extends Plant {
	private static final int STRENGTH = 10;

	public Hogweed(World world, Point position) {
		super(world, position, STRENGTH);
	}

	@Override
	public void action() {
		super.action();
		
		int xpos = getPosition().x, ypos = getPosition().y;
		int width = m_world.getColumns(), height = m_world.getRows();

		int nx = (xpos - 1 < 0 ? xpos - 1 + width : (xpos - 1) % width);
		Entity e = m_world.getEntityAt(nx, ypos);
		if (e instanceof Animal && !(e instanceof Hogweed) && !(e instanceof CyberSheep))
			e.kill();

		nx = (xpos + 1 < 0 ? xpos + 1 + width : (xpos + 1) % width);
		e = m_world.getEntityAt(nx, ypos);
		if (e instanceof Animal && !(e instanceof Hogweed) && !(e instanceof CyberSheep))
			e.kill();

		int ny = (ypos - 1 < 0 ? ypos - 1 + height : (ypos - 1) % height);
		e = m_world.getEntityAt(xpos, ny);
		if (e instanceof Animal && !(e instanceof Hogweed) && !(e instanceof CyberSheep))
			e.kill();

		ny = (ypos + 1 < 0 ? ypos + 1 + height : (ypos + 1) % height);
		e = m_world.getEntityAt(xpos, ny);
		if (e instanceof Animal && !(e instanceof Hogweed) && !(e instanceof CyberSheep))
			e.kill();
	}
	
	@Override
	public void collision(Entity other) {
		if (!(other instanceof CyberSheep))
			other.kill();
	}

	@Override
	public ImageID getImageID() {
		return ImageID.HOGWEED;
	}

}
