package com.kostu96.bots.utils;

import java.awt.Image;
import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import javax.imageio.ImageIO;

public class ImageManager {
	public enum ImageID {
		EMPTY,
		ANTELOPE,
		CYBERSHEEP,
		FOX,
		HUMAN,
		SHEEP,
		TURTLE,
		WOLF,
		BELLADONA,
		DANDELION,
		GRASS,
		GUARANA,
		HOGWEED
	}
	
	private static Map<ImageID, Image> map = new HashMap<>();
	
	private static File getFile(ImageID id) {
		switch (id) {
		case EMPTY: return new File("assets/empty.png");
		case ANTELOPE: return new File("assets/antelope.png");
		case BELLADONA: return new File("assets/belladonna.png");
		case CYBERSHEEP: return new File("assets/cybersheep.png");
		case DANDELION: return new File("assets/dandelion.png");
		case FOX: return new File("assets/fox.png");
		case GRASS: return new File("assets/grass.png");
		case GUARANA: return new File("assets/guarana.png");
		case HOGWEED: return new File("assets/hogweed.png");
		case HUMAN: return new File("assets/human.png");
		case SHEEP: return new File("assets/sheep.png");
		case TURTLE: return new File("assets/turtle.png");
		case WOLF: return new File("assets/wolf.png");
		default: return null;
		}
	}
	
	public static Image getImage(ImageID id) throws IOException {
		Image img = map.get(id);
		if (img == null) {
			img = ImageIO.read(getFile(id));
			map.put(id, img);
		}
		return img;
	}
}
