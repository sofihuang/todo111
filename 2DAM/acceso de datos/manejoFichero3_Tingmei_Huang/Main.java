import java.io.*;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;

public class Main {
    public static void main(String[] args) {

        detectaCodificacion();


        convertirAISO8859();
        convertirAUTF8();
        convertirAUTF32();




    }

    public static void detectaCodificacion(){

        String rutaArchivo = "src/quijote.txt";
        String codificacion = "Windows-1252";

        try {
            FileInputStream archivoInputStream = new FileInputStream(rutaArchivo);
            InputStreamReader inputStreamReader = new InputStreamReader(archivoInputStream, Charset.forName(codificacion));
            BufferedReader bufferedReader = new BufferedReader(inputStreamReader);

            String linea;
            while ((linea = bufferedReader.readLine()) != null) {
                System.out.println(linea);
            }

            bufferedReader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    public static void convertirAISO8859() {
        String file = "src/quijote.txt";
        String ISO8859file = "quijote-iso8859.txt";

        Charset utf8Charset = StandardCharsets.UTF_8;
        Charset iso8859Charset = Charset.forName("ISO-8859-1");

        try (
                BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(file), utf8Charset));
                BufferedWriter iso8859Writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(ISO8859file), iso8859Charset))
        ) {
            String linea;
            while ((linea = reader.readLine()) != null) {
                iso8859Writer.write(linea);
                iso8859Writer.newLine();
            }

            iso8859Writer.close();
            System.out.println("Archivo convertido a ISO-8859-1 con éxito.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void convertirAUTF8() {
        String file = "src/quijote.txt";
        String UTF8file = "quijote-utf8.txt";

        Charset utf8Charset = StandardCharsets.UTF_8;

        try (
                BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(file), utf8Charset));
                BufferedWriter utf8Writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(UTF8file), utf8Charset))
        ) {
            String linea;
            while ((linea = reader.readLine()) != null) {
                utf8Writer.write(linea);
                utf8Writer.newLine();
            }

            utf8Writer.close();
            System.out.println("Archivo convertido a UTF-8 con éxito.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void convertirAUTF32() {
        String file = "src/quijote.txt";
        String UTF32file = "quijote-utf32.txt";

        Charset utf32Charset = Charset.forName("UTF-32");

        try (
                BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(file), utf32Charset));
                BufferedWriter utf32Writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(UTF32file), utf32Charset))
        ) {
            String linea;
            while ((linea = reader.readLine()) != null) {
                utf32Writer.write(linea);
                utf32Writer.newLine();
            }

            utf32Writer.close();
            System.out.println("Archivo convertido a UTF-32 con éxito.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

