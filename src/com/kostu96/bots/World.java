package com.kostu96.bots;

import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.BoxLayout;
import javax.swing.JPanel;

public class World extends JPanel {
	private static final long serialVersionUID = 1L;
	
	private int columns, rows;
	
	public World(int columns, int rows) throws IOException {
		super();
		
		this.columns = columns;
		this.rows = rows;
		
		setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
		for (int i = 0; i < rows; ++i) {
			JPanel row = new JPanel();
			row.setLayout(new BoxLayout(row, BoxLayout.X_AXIS));
			row.setAlignmentX(LEFT_ALIGNMENT);
			for (int j = 0; j < columns; ++j) {
				row.add(new Cell(ImageIO.read(new File("assets/empty.png"))));
			}
			add(row);
		}
	}
	
	public int getColumns() { return columns; }
	
	public int getRows() { return rows; }
}
