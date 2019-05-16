package com.kostu96.bots;

import java.awt.Color;
import java.awt.Image;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;

public class Cell extends JButton {
	private static final long serialVersionUID = 1L;
	
	Cell(Image image) {
		super(new ImageIcon(image));
		
		setBorder(BorderFactory.createLineBorder(Color.lightGray, 1));

		addMouseListener(new MouseAdapter() {

			@Override
			public void mouseEntered(MouseEvent e) {
				setBorder(BorderFactory.createLineBorder(Color.gray, 1));
			}

			@Override
			public void mouseExited(MouseEvent e) {
				setBorder(BorderFactory.createLineBorder(Color.lightGray, 1));
			}
		});
	}

}
