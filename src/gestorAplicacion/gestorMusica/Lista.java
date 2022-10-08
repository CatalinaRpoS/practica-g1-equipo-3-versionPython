package gestorAplicacion.gestorMusica;

import java.util.ArrayList;

import gestorAplicacion.gestorPersonas.*;

public class Lista {
	private ArrayList<Cancion> lista;
	private Usuario usuario;
	private String nombre;
	
	public Lista(String nombre, Usuario usuario) {
		lista=new ArrayList<>();
		this.usuario = usuario;
		this.nombre=nombre;
	}
	
	public Lista(String nombre,ArrayList<Cancion> lista, Usuario usuario) {
		this.lista=lista;
		this.usuario = usuario;
		this.nombre=nombre;
	}
	
	public ArrayList<Cancion> getListas() {
		return lista;
	}

	public void setListas(ArrayList<Cancion> lista) {
		this.lista = lista;
	}

	public Usuario getUsuario() {
		return usuario;
	}

	public void setUsuario(Usuario usuario) {
		this.usuario = usuario;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	
	public String agregarCancion(Cancion cancion) {
		lista.add(cancion);
		return "Se ha agregado la canción "+cancion.getNombre()+" a la lista "+nombre+" con exito";
	}
	
	public String eliminarCancion(Cancion cancion) {
		for (int i=0;i<lista.size();i++) {
			if (cancion==lista.get(i)) {
				lista.remove(i);
			}
		}
		return "Se ha eliminado la canción "+cancion.getNombre()+" de la lista "+nombre+"con exito";
	}
	
	public String ToString() {
		return "Reproduciendo la lista "+nombre;
	}
}
