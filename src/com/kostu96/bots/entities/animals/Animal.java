package com.kostu96.bots.entities.animals;

import java.util.Vector;

import com.kostu96.bots.World;
import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.entities.plants.Plant;
import com.kostu96.bots.utils.Point;
import com.kostu96.bots.utils.Randmizer;

public abstract class Animal extends Entity {
	
	public Animal(World world, Point position, int strength, int initiative) {
		super(world, position, strength, initiative);
	}

	@Override
	public void action() {
		int vorh = Randmizer.getInt(0, 1), norp = Randmizer.getInt(0, 1);
		
		if (vorh == 1)
			move(0, norp == 1 ? -1 : 1);
		else
			move(norp == 1 ? -1 : 1, 0);
	}
	
	public void collision(Entity other) {
		if (other instanceof Plant) {
			other.kill();
			
			// TODO: messages
			System.out.println(other.getClassName() + " was eaten by " + getClassName());
			
			other.collision(this);
		}
		else if (other.getClass() == this.getClass()) {
			moveToPrevPosition();
			
			Vector<Point> arr = m_world.getFreeSpaceAround(getPosition());

			if (arr.size() > 0) {
				Point p = arr.get(Randmizer.getInt(0, arr.size() - 1));
				m_world.spawnEntity(getClassName(), p);
			}
		}
		else if (other.dodgedAttack(getStrength())) {
			moveToPrevPosition();
		}
		else if (other.getStrength() <= getStrength()) {
			other.kill();
			
			// TODO: messages
			System.out.println(other.getClassName() + " was eaten by " + getClassName());
		}
		else {
			kill();
			// TODO: messages
			System.out.println(getClassName() + " was eaten by " + other.getClassName());
		}
	}
}
