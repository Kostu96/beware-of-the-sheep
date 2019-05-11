package com.kostu96.bots;

import javax.swing.JFrame;

public final class App extends JFrame {
	private static final long serialVersionUID = 1L;

	public App() {
		super();
		
		add(new Board());
	        
	    setTitle("Beware Of The Sheep");
	    setSize(1280, 720);
	    setLocationRelativeTo(null);
	    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	    setVisible(true);
	}
	
	public static void main(String[] args) {
		new App();
	}

}
