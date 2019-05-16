package com.kostu96.bots;

import java.awt.EventQueue;
import java.io.IOException;

import javax.swing.JFrame;

public final class App extends JFrame {
	private static final long serialVersionUID = 1L;

	private World world;
	
	public App() throws IOException {
		super();
		
		world = new World(18, 18);
		add(world);
		
	    setTitle("Beware Of The Sheep");
	    setSize(1280, 720);
	    setResizable(false);
	    setLocationRelativeTo(null);
	    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	    setVisible(true);
	}
	
	public static void main(String[] args) {
		EventQueue.invokeLater(() -> {
            try {
				new App();
			} catch (IOException e) {
				e.printStackTrace();
			}
        });
	}
}
