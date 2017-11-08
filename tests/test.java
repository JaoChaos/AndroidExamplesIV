

import java.util.ArrayList;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Assert;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

public int existeFichero(){
String sFichero = "AndroidExamplesIV/src";
File fichero = new File(sFichero);

if (fichero.exists())
  return 0;
else
  return 1;
}
