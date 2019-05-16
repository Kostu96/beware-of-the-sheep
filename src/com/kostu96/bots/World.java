package com.kostu96.bots;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Vector;
import java.util.function.Predicate;

import javax.swing.BoxLayout;
import javax.swing.JPanel;

import com.kostu96.bots.entities.Entity;
import com.kostu96.bots.entities.animals.*;
import com.kostu96.bots.entities.plants.*;
import com.kostu96.bots.utils.ImageManager;
import com.kostu96.bots.utils.ImageManager.ImageID;
import com.kostu96.bots.utils.Point;

public class World extends JPanel {
	private static final long serialVersionUID = 1L;
	
	private int columns, rows;
	private List<Entity> entities;
	private boolean[][] area;
	
	private void addEntity(Entity e) {
		entities.add(e);
		area[e.getPosition().x][e.getPosition().y] = true;
		
		// TODO: messages
		System.out.println(e.getClassName() + " was spawned at " + e.getPosition());
	}
	
	private void removeKilledEntities() {
		entities.removeIf(new Predicate<>() {
			@Override
			public boolean test(Entity t) {
				if (!t.isAlive()) {
					Point p = t.getPosition();
					area[p.x][p.y]= false; 
					return true;
				}
				return false;
			}
		});
	}
	
	private void sortEntities() {
		entities.sort(new Comparator<Entity>() {
			@Override
			public int compare(Entity o1, Entity o2) {
				if (o1.getInitiative() > o2.getInitiative())
					return -1;
				if (o1.getInitiative() < o2.getInitiative())
					return 1;
				if (o1.getLifeTime() > o2.getLifeTime())
					return -1;
				if (o1.getLifeTime() < o2.getLifeTime())
					return 1;
				return 0;
			}
		});
	}
	
	public World(int columns, int rows) throws IOException {
		super();
		
		this.columns = columns;
		this.rows = rows;
		
		entities = new ArrayList<>();
		area = new boolean[columns][rows];
		
		addEntity(new Grass(this, new Point(1, 1)));
		addEntity(new Grass(this, new Point(2, 1)));
		addEntity(new Grass(this, new Point(3, 1)));
		addEntity(new Dandelion(this, new Point(5, 5)));
		addEntity(new Human(this, new Point(10, 10)));
				
		setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
		for (int i = 0; i < rows; ++i) {
			JPanel row = new JPanel();
			row.setLayout(new BoxLayout(row, BoxLayout.X_AXIS));
			row.setAlignmentX(LEFT_ALIGNMENT);
			for (int j = 0; j < columns; ++j) {
				Cell c;
				if (area[j][i])	{
					Entity e = getEntityAt(j, i);
					c = new Cell(ImageManager.getImage(e.getImageID()));
					c.setToolTipText(e.getClassName());
					row.add(c);
				}
				else {
					c = new Cell(ImageManager.getImage(ImageID.EMPTY));
					row.add(c);
				}
			}
			add(row);
		}
	}
	
	public int getColumns() { return columns; }
	
	public int getRows() { return rows; }
	
	public void turn() {
		removeKilledEntities();
		sortEntities();
		
		for (Entity e : entities)
			if (e.isAlive()) {
				e.action();
				Point p = e.getPosition();
				Entity x = getEntityAt(p.x, p.y);
				if (x != null && x != e)
					e.collision(x);
				e.incrementLifeTime();
			}
	}
	
	public Entity getEntityAt(int x, int y) {
		for(Entity e : entities)
			if(e.getPosition().x == x && e.getPosition().y == y)
		    	return e;
		
		return null;
	}
	
	public Vector<Point> getFreeSpaceAround(Point pos) {
		Vector<Point> arr = new Vector<>();

		int nx = (pos.x - 1 < 0 ? pos.x - 1 + columns : (pos.x - 1) % columns);
		if (!area[nx][pos.y])
			arr.add(new Point(nx, pos.y));

		nx = (pos.x + 1 < 0 ? pos.x + 1 + columns : (pos.x + 1) % columns);
		if (!area[nx][pos.y])
			arr.add(new Point(nx, pos.y));

		int ny = (pos.y - 1 < 0 ? pos.y - 1 + rows : (pos.y - 1) % rows);
		if (!area[pos.x][ny])
			arr.add(new Point(pos.x, ny));

		ny = (pos.y + 1 < 0 ? pos.y + 1 + rows : (pos.y + 1) % rows);
		if (!area[pos.x][ny])
			arr.add(new Point(pos.x, ny));

		return arr; 
	}
	
	public void spawnEntity(String className, Point position) {
		switch (className) {
		case "Antelope": addEntity(new Antelope(this, position)); break;
		case "CyberSheep": addEntity(new Antelope(this, position)); break;
		case "Fox": addEntity(new Antelope(this, position)); break;
		case "Human": addEntity(new Antelope(this, position)); break;
		case "Sheep": addEntity(new Antelope(this, position)); break;
		case "Turtle": addEntity(new Antelope(this, position)); break;
		case "Wolf": addEntity(new Antelope(this, position)); break;
		case "Belladonna": addEntity(new Antelope(this, position)); break;
		case "Dandelion": addEntity(new Antelope(this, position)); break;
		case "Grass": addEntity(new Antelope(this, position)); break;
		case "Guarana": addEntity(new Antelope(this, position)); break;
		case "Hogweed": addEntity(new Antelope(this, position)); break;
		default: break;
		}
	}
}
