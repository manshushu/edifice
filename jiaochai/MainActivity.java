// 创建内部文件
FileOutputStream fos = openFileOutput("my_file.txt", Context.MODE_PRIVATE);
String data = "Hello world!";
fos.write(data.getBytes());
fos.close();

// 读取内部文件
FileInputStream fis = openFileInput("my_file.txt");
InputStreamReader isr = new InputStreamReader(fis);
char[] inputBuffer = new char[fis.available()];
isr.read(inputBuffer);
String data = new String(inputBuffer);
isr.close();
fis.close();

// 创建外部文件
File file = new File(getExternalFilesDir(null), "my_file.txt");
FileOutputStream fos = new FileOutputStream(file);
String data = "Hello world!";
fos.write(data.getBytes());
fos.close();

// 读取外部文件
File file = new File(getExternalFilesDir(null), "my_file.txt");
FileInputStream fis = new FileInputStream(file);
InputStreamReader isr = new InputStreamReader(fis);
char[] inputBuffer = new char[fis.available()];
isr.read(inputBuffer);
String data = new String(inputBuffer);
isr.close();
fis.close();

// 创建资源文件
OutputStreamWriter osw = new OutputStreamWriter(openFileOutput("my_file.txt",Context.MODE_PRIVATE));
osw.write("Hello world!");
osw.close();

// 读取资源文件
InputStreamReader isr = new InputStreamReader(getResources().openRawResource(R.raw.my_file));
char[] inputBuffer = new char[isr.available()];
isr.read(inputBuffer);
String data = new String(inputBuffer);
isr.close();
