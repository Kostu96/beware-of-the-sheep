package com.kostu96.bots;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Vector;
import java.util.function.Predicate;

import javax.swing.BoxLayout;
import javax.swing.ImageIcon;
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
	private List<Cell> tiles;
	private boolean[][] area;
	
	private void addEntity(Entity e) {
		Point p = e.getPosition();
		entities.add(e);
		area[p.x][p.y] = true;
		
		// TODO: messages
		System.out.println(e.getClassName() + " was spawned at " + p);
	}
	
	private void updateImages() {
		for (int i = 0; i < rows; ++i) {
			for (int j = 0; j < columns; ++j) {
				Cell c = getTileAt(j, i);
				Entity e = getEntityAt(j, i);
				try {
					if (e != null) {
						c.setIcon(new ImageIcon(ImageManager.getImage(e.getImageID())));
						c.setToolTipText(e.getClassName());
					} else {
						c.setIcon(new ImageIcon(ImageManager.getImage(ImageID.EMPTY)));
						c.setToolTipText(null);
					}
				} catch (IOException e1) {
					e1.printStackTrace();
				}
			}
		}
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
	
	private Cell getTileAt(int x, int y) {
		return tiles.get(y * columns + x);
	}
	
	public World(int columns, int rows) throws IOException {
		super();
		
		this.columns = columns;
		this.rows = rows;
		
		entities = new ArrayList<>();
		area = new boolean[columns][rows];
		tiles = new ArrayList<>();
		
		addEntity(new Antelope(this, new Point(1, 1)));
		addEntity(new Antelope(this, new Point(1, 3)));
		addEntity(new Fox(this, new Point(4, 5)));
		addEntity(new Fox(this, new Point(6, 5)));
		addEntity(new Sheep(this, new Point(4, 7)));
		addEntity(new Sheep(this, new Point(4, 9)));
		addEntity(new Turtle(this, new Point(5, 9)));
		addEntity(new Turtle(this, new Point(6, 9)));
		addEntity(new Wolf(this, new Point(6, 11)));
		addEntity(new Wolf(this, new Point(6, 13)));
		addEntity(new Belladonna(this, new Point(2, 13)));
		addEntity(new Dandelion(this, new Point(3, 15)));
		addEntity(new Grass(this, new Point(4, 17)));
		addEntity(new Guarana(this, new Point(12, 12)));
		addEntity(new Hogweed(this, new Point(5, 5)));
		//addEntity(new Human(this, new Point(10, 10)));
				
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
				tiles.add(c);
			}
			add(row);
		}
	}
	
	public int getColumns() { return columns; }
	
	public int getRows() { return rows; }
	
	public void turn() {
		sortEntities();
		
		int size = entities.size();
		for (int i = 0; i < size; ++i) {
			Entity e = entities.get(i);
			if (e.isAlive()) {
				e.action();
				Point p = e.getPosition();
				Entity x = getEntityAt(p.x, p.y);
				if (x != null && x != e)
					x.collision(e);
				e.incrementLifeTime();
			}
		}
		removeKilledEntities();
		updateImages();
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
		case "CyberSheep": addEntity(new CyberSheep(this, position)); break;
		case "Fox": addEntity(new Fox(this, position)); break;
		case "Human": addEntity(new Human(this, position)); break;
		case "Sheep": addEntity(new Sheep(this, position)); break;
		case "Turtle": addEntity(new Turtle(this, position)); break;
		case "Wolf": addEntity( new Wolf(this, position)); break;
		case "Belladonna": addEntity(new Belladonna(this, position)); break;
		case "Dandelion": addEntity(new Dandelion(this, position)); break;
		case "Grass": addEntity(new Grass(this, position)); break;
		case "Guarana": addEntity(new Guarana(this, position)); break;
		case "Hogweed": addEntity(new Hogweed(this, position)); break;
		default: break;
		}
	}
}
