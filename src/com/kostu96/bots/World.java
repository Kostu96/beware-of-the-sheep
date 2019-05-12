package com.kostu96.bots;

import java.util.ArrayList;
import java.util.List;

import com.kostu96.bots.entities.Entity;

public class World {
	private int width;
	private int height;
	
	private List<Entity> m_entities = new ArrayList<>();
	
	public World(int width, int height) {
		this.width = width;
		this.height = height;
	}
	
	public int getWidth() { return width; }
	
	public int getHeight() { return height; }
	
	public void tick() {
		
	}
}
