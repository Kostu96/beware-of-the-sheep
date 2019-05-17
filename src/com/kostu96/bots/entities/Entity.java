package com.kostu96.bots.entities;

import com.kostu96.bots.World;
import com.kostu96.bots.utils.ImageManager.ImageID;
import com.kostu96.bots.utils.Point;

public abstract class Entity {
	private boolean m_isAlive;
	private Point m_position;
	private Point m_prevPosition;
	
	private int m_strength;
	private int m_initiative;
	private int m_lifeTime;
	
	protected World m_world;
	
	protected void move(int x, int y) {
		m_prevPosition = m_position;
		
		int width = m_world.getWidth();
		int height = m_world.getHeight();
		
		int newX = m_position.x + x;
		m_position.x = newX < 0 ? newX + width : newX % width;
		int newY = m_position.y + y;
		m_position.y = newY < 0 ? newY + height : newY % height;
	}
	
	protected void moveToPrevPosition() { move(m_prevPosition.x, m_prevPosition.y); }
	
	public Entity(World world, Point position, int strength, int initiative) {
		m_isAlive = true;
		m_world = world;
		m_position = position;
		m_strength = strength;
		m_initiative = initiative;
	}
	
	public boolean isAlive() { return m_isAlive; }
	
	public Point getPosition() { return m_position; }
	
	public int getStrength() { return m_strength; }
	
	public int getInitiative() { return m_initiative; }
	
	public int getLifeTime() { return m_lifeTime; }
	
	public void kill() { m_isAlive = false; }
	
	public void addStrength(int strength) { m_strength += strength; }
	
	public void incrementLifeTime() { ++m_lifeTime; }
	
	public boolean dodgeAttack(int strength) { return false; }
	
	abstract public void action();
	
	abstract public void collision(Entity other);
	
	abstract public ImageID getImageID();
	
	public String getClassName() {
		String name = getClass().getName();
		return name.substring(name.lastIndexOf('.') + 1);
	}

	public boolean dodgedAttack(int strength) {
		return false;
	}

}
