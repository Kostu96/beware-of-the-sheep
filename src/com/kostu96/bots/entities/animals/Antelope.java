package com.kostu96.bots.entities.animals;

import java.util.Vector;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.utils.ImageManager.ImageID;
import com.kostu96.bots.utils.Point;
import com.kostu96.bots.utils.Randmizer;

public class Antelope extends Animal {
	private static final int STRENGTH = 4;
	private static final int INITIATIVE = 4;
	
	public Antelope(World world, Point position) {
		super(world, position, STRENGTH, INITIATIVE);
	}

	@Override
	public void action() {
		int vorh = Randmizer.getInt(0, 1), norp = Randmizer.getInt(0, 1);
		
		if (vorh == 1)
			move(0, norp == 1 ? -2 : 2);
		else
			move(norp == 1 ? -2 : 2, 0);
	}
	
	@Override
	public void collision(Entity other) {
		int x = Randmizer.getInt(0, 1);
		if (x == 0)
			super.collision(other);
		else {
			Vector<Point> arr = m_world.getFreeSpaceAround(getPosition());
			if (arr.size() > 0) {
				Point p = arr.get(Randmizer.getInt(0, arr.size() - 1));
				move(p.x - getPosition().x, p.y - getPosition().y);
			}
			else
				super.collision(other);
		}
	}

	@Override
	public ImageID getImageID() {
		return ImageID.ANTELOPE;
	}

}
