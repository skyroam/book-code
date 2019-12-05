package wang;
/**
 * Description:
 * Program Name: <br>
 * Data: <br>
 * @author Wang Yixuan
 * @version 1.0
 */
public class Student
{
  /**
   * member field
   * name and id of student
   */
  public String name;
  public int id;

  /**
   * member method
   * set the name of student
   * @param name a string
   */
  public setName(String name)
  {
    this.name = name;
  }

  /**
   * member method
   * get the name of student
   * @return the string of name
   */
  public getName()
  {
    return this.name;
  }
}
