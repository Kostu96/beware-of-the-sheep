package com.kostu96.bots;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;

import javax.swing.JButton;
import javax.swing.JFrame;

public final class App extends JFrame {
	private static final long serialVersionUID = 1L;
	
	private World world;
	
	public App() throws IOException {
		super();
		
		world = new World(18, 18);
		add(world);
		
		JButton turnBtn = new JButton("Turn");
		turnBtn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) { world.turn(); }
		});
		add(turnBtn, BorderLayout.EAST);
		
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
