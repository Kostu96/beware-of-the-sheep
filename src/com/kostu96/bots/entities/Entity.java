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
		m_isAlive = true;
		
		m_prevPosition = m_position;
		
		int width = m_world.getWidth();
		int height = m_world.getHeight();
		
		m_position.x = x < 0 ? x + width : x % width;
		m_position.y = y < 0 ? y + height : y % height;
	}
	
	protected void moveToPrevPosition() { move(m_prevPosition.x, m_prevPosition.y); }
	
	public Entity(World world, Point position, int strength, int initiative) {
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

}
