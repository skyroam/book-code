package chapter1;
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
  public void setName(String name)
  {
    this.name = name;
  }

  /**
   * member method
   * get the name of student
   * @return the string of name
   */
  public String getName()
  {
    return this.name;
  }

  /**
   * member method
   * set the id of student
   * @param id an integer
   */
  public void setId(int id)
  {
    this.id = id;
  }

  /**
   * member method
   * get the id of student
   * @return the integer of id
   */
  public int getId()
  {
    return this.id;
  }
}
