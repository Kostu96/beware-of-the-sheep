package com.kostu96.bots;

import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public final class App extends JFrame {
	private static final long serialVersionUID = 1L;

	public App() {
		super();
		
		add(new Board());
		
		JPanel buttons = new JPanel();
		buttons.setLayout(new BoxLayout(buttons, BoxLayout.Y_AXIS));
		
		JButton newGameButton = new JButton("New Game");
		buttons.add(newGameButton);
	        
		add(buttons);
		
	    setTitle("Beware Of The Sheep");
	    setSize(1280, 720);
	    setResizable(false);
	    setLocationRelativeTo(null);
	    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	    setVisible(true);
	}
	
	public static void main(String[] args) {
		new App();
		
		World world = new World(20, 20);
		while (true)
		{
			world.tick();
		}
	}

}
