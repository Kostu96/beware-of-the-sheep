package com.kostu96.bots.entities.animals;

import java.util.Vector;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.utils.ImageManager.ImageID;
import com.kostu96.bots.utils.Point;
import com.kostu96.bots.utils.Randmizer;

public class Fox extends Animal {
	private static final int STRENGTH = 3;
	private static final int INITIATIVE = 7;

	public Fox(World world, Point position) {
		super(world, position, STRENGTH, INITIATIVE);
	}

	@Override
	public void action() {
		Vector<Point> dir = new Vector<>();

		int xpos = getPosition().x, ypos = getPosition().y;
		int width = m_world.getColumns(), height = m_world.getRows();

		int nx = (xpos - 1 < 0 ? xpos - 1 + width : (xpos - 1) % width);
		Entity e = m_world.getEntityAt(nx, ypos);
		if (e == null || e.getStrength() < getStrength())
			dir.add(new Point(nx, ypos));

		nx = (xpos + 1 < 0 ? xpos + 1 + width : (xpos + 1) % width);
		e = m_world.getEntityAt(nx, ypos);
		if (e == null || e.getStrength() < getStrength())
			dir.add(new Point(nx, ypos));

		int ny = (ypos - 1 < 0 ? ypos - 1 + height : (ypos - 1) % height);
		e = m_world.getEntityAt(nx, ypos);
		if (e == null || e.getStrength() < getStrength())
			dir.add(new Point(xpos, ny));

		ny = (ypos + 1 < 0 ? ypos + 1 + height : (ypos + 1) % height);
		e = m_world.getEntityAt(nx, ypos);
		if (e == null || e.getStrength() < getStrength())
			dir.add(new Point(xpos, ny));

		Point d = dir.get(Randmizer.getInt(0, dir.size() - 1));
		move(d.x - xpos, d.y - ypos);
	}

	@Override
	public ImageID getImageID() {
		return ImageID.FOX;
	}

}
