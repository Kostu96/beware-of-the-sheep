package com.kostu96.bots.entities.plants;

import java.util.Vector;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.utils.Point;
import com.kostu96.bots.utils.Randmizer;

public abstract class Plant extends Entity {

	public Plant(World world, Point position, int strength) {
		super(world, position, strength, 0);
	}

	@Override
	public void action() {
		Vector<Point> arr = m_world.getFreeSpaceAround(getPosition());
		
		int c = Randmizer.getInt(0, 8);
		if (c == 0 && arr.size() > 0) {
			Point p = arr.get(Randmizer.getInt(0, arr.size()));
			m_world.spawnEntity(getClassName(), p);
		}
	}
	
	@Override
	public void collision(Entity other) {}
}
